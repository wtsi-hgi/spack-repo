# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPakpmics2018(RPackage):
	"""Multiple Indicator Cluster Survey (MICS) 2017-18 Data for
Punjab, Pakistan

	Provides data set and function for exploration of Multiple Indicator Cluster Survey (MICS) 2017-18 data for Punjab, Pakistan. The results of the present survey are critically important for the purposes of SDG monitoring, as the survey produces information on 32 global SDG indicators. The data was collected from 53,840 households selected at the second stage with systematic random sampling out of a sample of 2,692 clusters selected using Probability Proportional to size sampling. Six questionnaires were used in the survey: (1) a household questionnaire to collect basic demographic information on all de jure household members (usual residents), the household, and the dwelling; (2) a water quality testing questionnaire administered in three households in each cluster of the sample; (3) a questionnaire for individual women administered in each household to all women age 15-49 years; (4) a questionnaire for individual men administered in every second household to all men age 15-49 years; (5) an under-5 questionnaire, administered to mothers (or caretakers) of all children under 5 living in the household; and (6) a questionnaire for children age 5-17 years, administered to the mother (or caretaker) of one randomly selected child age 5-17 years living in the household (<http://www.mics.unicef.org/surveys>).
	"""
	
	homepage = "https://github.com/myaseen208/PakPMICS2018"
	cran = "PakPMICS2018" 

	version("1.0.0", md5="f5845be57041daa27dd24b687c6ef995", url="https://cran.r-project.org/src/contrib/PakPMICS2018_1.0.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
