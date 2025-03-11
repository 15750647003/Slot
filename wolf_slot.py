import tkinter as tk
from tkinter import ttk
import random

ICONS = {
    "★": 10, "☀": 20, "☁": 15, "❄": 5,
    "❤": 25, "⚡": 40, "♫": 8, "✿": 12
}


class MultiComboGame:
    def __init__(self, root):
        self.root = root
        self.root.title("多组合计分版")

        # 游戏状态
        self.total_score = 0
        self.current_score = 0
        self.grid_data = []

        # 创建界面
        self.create_widgets()
        self.set_initial_state()

    def create_widgets(self):
        """创建界面组件"""
        # 控制面板
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(pady=10)

        self.btn_start = ttk.Button(
            self.control_frame,
            text="开始新游戏",
            command=self.start_game
        )
        self.btn_start.pack(side=tk.LEFT, padx=5)

        self.btn_next = ttk.Button(
            self.control_frame,
            text="继续下一轮",
            state=tk.DISABLED,
            command=self.next_round
        )
        self.btn_next.pack(side=tk.LEFT, padx=5)

        # 分数显示
        self.score_frame = ttk.LabelFrame(self.root, text="分数统计")
        self.score_frame.pack(fill=tk.X, padx=10, pady=5)

        self.lbl_total = ttk.Label(
            self.score_frame,
            text="历史总分：0"
        )
        self.lbl_total.pack(side=tk.LEFT, padx=20)

        self.lbl_current = ttk.Label(
            self.score_frame,
            text="当轮得分：0"
        )
        self.lbl_current.pack(side=tk.LEFT, padx=20)

        # 图标展示区
        self.grid_frame = ttk.Frame(self.root)
        self.grid_frame.pack(padx=10, pady=10)

        self.grid_labels = []
        for row in range(3):
            row_labels = []
            for col in range(5):
                lbl = ttk.Label(
                    self.grid_frame,
                    text="",
                    width=4,
                    relief="solid",
                    anchor=tk.CENTER,
                    font=('Arial', 18)
                )
                lbl.grid(row=row, column=col, padx=2, pady=2)
                row_labels.append(lbl)
            self.grid_labels.append(row_labels)

    def set_initial_state(self):
        """初始化状态"""
        for row in self.grid_labels:
            for lbl in row:
                lbl.config(text="?", foreground="gray")

    def generate_grid(self):
        """生成新的图标网格"""
        self.grid_data = []
        print("\n" + "=" * 40)
        print("生成新网格：")
        for _ in range(3):
            row = [random.choice(list(ICONS.keys())) for _ in range(5)]
            self.grid_data.append(row)
            print(" | ".join(row))

        # 更新显示
        for row_idx, row in enumerate(self.grid_data):
            for col_idx, icon in enumerate(row):
                self.grid_labels[row_idx][col_idx].config(
                    text=icon,
                    foreground="black"
                )

    def calculate_score(self):
        """仅计算列式连线得分"""
        print("\n开始计算得分：")
        self.current_score = self.check_bonus()
        self.total_score += self.current_score

    def check_bonus(self):
        """多组合独立计分算法（带详细步骤输出）"""
        bonus = 0
        combo_records = []
        all_icons = set(icon for row in self.grid_data for icon in row)

        print("\n" + "=" * 50)
        print("开始详细计分流程：")

        # 遍历所有可能的3列组合
        for start_col in range(3):
            end_col = start_col + 2
            current_range = f"列{start_col + 1}-{end_col + 1}"
            print(f"\n▶ 检查 {current_range} 组合：")

            found_any = False  # 标记是否找到有效组合

            # 检查每个可能存在的图标
            for icon in all_icons:
                print(f"\n▷ 正在检查 [{icon}]...")
                valid = True
                col_details = []

                # 检查每一列
                for col_offset in range(3):
                    actual_col = start_col + col_offset
                    column_icons = set(self.grid_data[row][actual_col] for row in range(3))
                    has_icon = icon in column_icons
                    col_details.append(f"列{actual_col + 1}: {'✅' if has_icon else '❌'}")

                    if not has_icon:
                        valid = False

                    # 打印每列检查结果
                    print(f"  列{actual_col + 1}包含{icon}？ {'是' if has_icon else '否'} "
                          f"({', '.join(column_icons)})")

                if valid:
                    score = ICONS[icon] * 10
                    bonus += score
                    record = f"{icon}在{current_range} → {score}分"
                    combo_records.append(record)
                    found_any = True
                    print(f"  🎉 有效组合！得分：{ICONS[icon]} × 10 = {score}")
                else:
                    print(f"  ❗ 无效组合：{', '.join(col_details)}")

            if not found_any:
                print(f"  ⚠ 本组合未找到任何有效连线")

        # 打印最终汇总
        print("\n" + "=" * 50)
        print("得分汇总：")
        if combo_records:
            for i, record in enumerate(combo_records, 1):
                print(f"{i}. {record}")
            print(f"\n总奖励分：{' + '.join(str(int(record.split('→').split('分'))) for record in combo_records)} = {bonus}")
        else:
            print("⚠ 未发现有效连线组合")

        return bonus

    def start_game(self):
        """开始新游戏"""
        print("===== 新游戏开始 =====")
        self.total_score = 0
        self.current_score = 0
        self.update_scores()
        self.btn_start.config(state=tk.DISABLED)
        self.btn_next.config(state=tk.NORMAL)
        self.next_round()

    def next_round(self):
        """进入下一轮"""
        self.generate_grid()
        self.calculate_score()
        self.update_scores()

        # 显示得分详情
        result_window = tk.Toplevel(self.root)
        result_window.title("本轮结果")

        ttk.Label(result_window, text=f"列式奖励：{self.current_score}").pack(padx=20, pady=5)
        ttk.Label(result_window, text=f"当轮得分：{self.current_score}", font=('Arial', 12, 'bold')).pack(padx=20, pady=5)

        ttk.Button(
            result_window,
            text="确定",
            command=result_window.destroy
        ).pack(pady=10)

    def update_scores(self):
        """更新分数显示"""
        self.lbl_total.config(text=f"历史总分：{self.total_score}")
        self.lbl_current.config(text=f"当轮得分：{self.current_score}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    game = MultiComboGame(root)
    root.mainloop()

