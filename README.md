# Gacha-RNG-Analyzer# Video Game RNG & Drop Rate Analyzer

## Overview
This is a lightweight Python command-line tool designed to analyze RNG (Random Number Generation) mechanics in modern gaming. It calculates the cumulative probability of obtaining a specific item over multiple attempts.

## The Math Behind the Tool
Many users fall victim to the Gambler's Fallacy, assuming that a 1% drop rate means an item is guaranteed in 100 attempts. This tool utilizes the probability of independent events to calculate the actual number of attempts required to reach a specific confidence threshold.

It solves for `n` (number of pulls) using the expected value formula:
`1 - (1 - P(Drop))^n = Target Probability`

## Proof of Work
This repository was created as an exercise in algorithmic thinking and probability analysis, mapping mathematical concepts to practical software engineering applications.
