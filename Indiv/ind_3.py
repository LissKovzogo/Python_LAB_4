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

    for i, (team, point) in enumerate(sorted_teams,1):
        print(f"Место: {i} {team} {point}")