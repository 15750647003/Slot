// 'use client'
// import { useState } from 'react'
// import { Button } from "@/components/aily/Button"
// import { Card } from "@/components/aily/Card"
// import { Label } from "@/components/aily/Label"
//
// const ICONS = ['★', '☀', '☁', '❄', '❤', '⚡', '♫', '✿']
//
// export default function GamePage() {
//   const [totalScore, setTotalScore] = useState(0)
//   const [currentScore, setCurrentScore] = useState(0)
//   const [grid, setGrid] = useState<string[][]>([])
//   const [logs, setLogs] = useState<string[]>([])
//
//   const generateGrid = () => {
//     const newGrid = Array.from({ length: 3 }, () =>
//       Array.from({ length: 5 }, () => ICONS[Math.floor(Math.random() * ICONS.length)])
//     )
//     setGrid(newGrid)
//     return newGrid
//   }
//
//   const checkBonus = (gridData: string[][]) => {
//     let bonus = 0
//     const newLogs = []
//     const allIcons = [...new Set(gridData.flat())]
//
//     newLogs.push("开始详细计分流程：")
//
//     for (let startCol = 0; startCol < 3; startCol++) {
//       const endCol = startCol + 2
//       newLogs.push(`\n▶ 检查 列${startCol + 1}-${endCol + 1} 组合：`)
//
//       allIcons.forEach(icon => {
//         let valid = true
//         const colDetails = []
//
//         for (let colOffset = 0; colOffset < 3; colOffset++) {
//           const actualCol = startCol + colOffset
//           const columnIcons = new Set(gridData.map(row => row[actualCol]))
//           colDetails.push(`列${actualCol + 1}: ${columnIcons.has(icon) ? '✅' : '❌'}`)
//           valid = valid && columnIcons.has(icon)
//         }
//
//         if (valid) {
//           const score = 10 * (ICONS.indexOf(icon) + 1)
//           bonus += score
//           newLogs.push(`发现有效组合：${icon} → ${score}分`)
//         }
//       })
//     }
//
//     setLogs(prev => [...prev, ...newLogs])
//     return bonus
//   }
//
//   const handleStart = () => {
//     const newGrid = generateGrid()
//     const score = checkBonus(newGrid)
//     setCurrentScore(score)
//     setTotalScore(prev => prev + score)
//   }
//
//   return (
//     <div className="p-6 max-w-4xl mx-auto space-y-4">
//       <Card className="p-6">
//         <div className="flex gap-4">
//           <Button onClick={handleStart}>开始新游戏</Button>
//           <div className="space-y-1">
//             <Label>历史总分: {totalScore}</Label>
//             <Label>当轮得分: {currentScore}</Label>
//           </div>
//         </div>
//       </Card>
//
//       <Card className="p-6">
//         <div className="grid grid-cols-5 gap-2">
//           {grid.map((row, rowIndex) =>
//             row.map((icon, colIndex) => (
//               <div
//                 key={`${rowIndex}-${colIndex}`}
//                 className="border p-4 text-center text-2xl"
//               >
//                 {icon}
//               </div>
//             ))
//           )}
//         </div>
//       </Card>
//
//       <Card className="p-6 max-h-96 overflow-auto">
//         <pre className="text-sm">
//           {logs.join('\n')}
//         </pre>
//       </Card>
//     </div>
//   )
// }