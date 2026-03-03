# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIatscore(RPackage):
	"""Scoring Algorithm for the Implicit Association Test (IAT)

	This minimalist package is designed to quickly score raw data outputted from an Implicit Association Test (IAT; Greenwald, McGhee, & Schwartz, 1998) <doi:10.1037/0022-3514.74.6.1464>. IAT scores are calculated as specified by Greenwald, Nosek, and Banaji (2003) <doi:10.1037/0022-3514.85.2.197>. Outputted values can be interpreted as effect sizes. The input function consists of three arguments. First, indicate the name of the dataset to be analyzed. This is the only required input. Second, indicate the number of trials in your entire IAT (the default is set to 219, which is typical for most IATs). Last, indicate whether congruent trials (e.g., flowers and pleasant) or incongruent trials (e.g., guns and pleasant) were presented first for this participant (the default is set to congruent). The script will tell you how long it took to run the code, the effect size for the participant, and whether that participant should be excluded based on the criteria outlined by Greenwald et al. (2003). Data files should consist of six columns organized in order as follows: Block (0-6), trial (0-19 for training blocks, 0-39 for test blocks), category (dependent on your IAT), the type of item within that category (dependent on your IAT), a dummy variable indicating whether the participant was correct or incorrect on that trial (0=correct, 1=incorrect), and the participant’s reaction time (in milliseconds). Three sample datasets are included in this package (labeled 'IAT', 'TooFastIAT', and 'BriefIAT') to practice with.
	"""
	
	cran = "IATScore" 

	version("0.1.1", md5="1034b3404b6f72ade1aef165a9e25d6c")

