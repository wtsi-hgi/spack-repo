# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPakpmics2018hh(RPackage):
	"""Multiple Indicator Cluster Survey (MICS) 2017-18 Household
Questionnaire Data for Punjab, Pakistan

	Provides data set and function for exploration of Multiple Indicator Cluster Survey (MICS) 2017-18 Household questionnaire data for Punjab, Pakistan. The results of the present survey are critically important for the purposes of Sustainable Development Goals (SDGs) monitoring, as the survey produces information on 32 global Sustainable Development Goals (SDGs) indicators. The data was collected from 53,840 households selected at the second stage with systematic random sampling out of a sample of 2,692 clusters selected using probability proportional to size sampling. Six questionnaires were used in the survey: (1) a household questionnaire to collect basic demographic information on all de jure household members (usual residents), the household, and the dwelling; (2) a water quality testing questionnaire administered in three households in each cluster of the sample; (3) a questionnaire for individual women administered in each household to all women age 15-49 years; (4) a questionnaire for individual men administered in every second household to all men age 15-49 years; (5) an under-5 questionnaire, administered to mothers (or caretakers) of all children under 5 living in the household; and (6) a questionnaire for children age 5-17 years, administered to the mother (or caretaker) of one randomly selected child age 5-17 years living in the household (<http://www.mics.unicef.org/surveys>).
	"""
	
	homepage = "https://github.com/myaseen208/PakPMICS2018hh"
	cran = "PakPMICS2018hh" 

	version("0.1.0", md5="67ce4df12781dde20ad8673567c0b1c9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
