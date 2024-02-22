# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIatanalytics(RPackage):
	"""Compute Effect Sizes and Reliability for Implicit Association
Test (IAT) Data

	Quickly score raw data outputted from an Implicit Association Test (IAT; Greenwald, McGhee, & Schwartz, 1998) <doi:10.1037/0022-3514.74.6.1464>. IAT scores are calculated as specified by Greenwald, Nosek, and Banaji (2003) <doi:10.1037/0022-3514.85.2.197>.    The output of this function is a data frame that consists of four rows containing the following information: (1) the overall IAT effect size for the participant's dataset, (2) the effect size calculated for odd trials only, (3) the effect size calculated for even trials only, and (4) the proportion of trials with reaction times under 300ms (which is important for exclusion purposes). Items (2) and (3) allow for a measure of the internal consistency of the IAT. Specifically, you can use the subsetted IAT effect sizes for odd and even trials to calculate Cronbach's alpha across participants in the sample.    The input function consists of three arguments. First, indicate the name of the dataset to be analyzed. This is the only required input. Second, indicate the number of trials in your entire IAT (the default is set to 220, which is typical for most IATs). Last, indicate whether congruent trials (e.g., flowers and pleasant) or incongruent trials (e.g., guns and pleasant) were presented first for this participant (the default is set to congruent).    Data files should consist of six columns organized in order as follows: Block (0-6), trial (0-19 for training blocks, 0-39 for test blocks), category (dependent on your IAT), the type of item within that category (dependent on your IAT), a dummy variable indicating whether the participant was correct or incorrect on that trial (0=correct, 1=incorrect), and the participant’s reaction time (in milliseconds).    A sample dataset (titled 'sampledata') is included in this package to practice with.
	"""
	
	cran = "IATanalytics" 

	version("0.1.1", md5="eb30e127cd6136ac0e043518b6cadd90")

