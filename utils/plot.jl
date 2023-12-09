using CSV
using DataFrames
using Plots

function plot_performance(csv_file)
    data = CSV.File(csv_file) |> DataFrame
    plot(data.Date, data."Total Habit Score", label="Total Habit Score", xlabel="Date", ylabel="Score", title="Habit Score Over Time", legend=:topleft)
end

csv_file = "/path/to/your/spreadsheet/habit_results.csv"
plot_performance(csv_file)
