#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    teams = (
        ("Команда А", 15),
        ("Команда Б", 12),
        ("Команда В", 18),
        ("Команда Г", 10),
        ("Команда Д", 14)
    )

    sorted_teams = sorted(teams, key=lambda x: x[1], reverse=True)
    print(sorted_teams)
    for i, (team, point) in enumerate(sorted_teams):
        # print(f"Место: {i+1} {team} {point}")
        print(f"Место: {i + 1} {sorted_teams[i][0]} {sorted_teams[i][1]}")
        # print(f"Место: {i + 1} {sorted_teams[i]} ")