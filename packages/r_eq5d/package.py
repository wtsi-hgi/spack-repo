# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REq5d(RPackage):
	"""Methods for Analysing 'EQ-5D' Data and Calculating 'EQ-5D' Index
Scores

	EQ-5D is a popular health related quality of life instrument used 
    in the clinical and economic evaluation of health care. Developed by the 
    EuroQol group <https://euroqol.org/>, the instrument consists of two 
    components: health state description and evaluation. For the description 
    component a subject self-rates their health in terms of five dimensions; 
    mobility, self-care, usual activities, pain/discomfort, and 
    anxiety/depression using either a three-level (EQ-5D-3L,
    <https://euroqol.org/information-and-support/euroqol-instruments/eq-5d-3l/>) or a five-level
    (EQ-5D-5L, <https://euroqol.org/information-and-support/euroqol-instruments/eq-5d-5l/>) 
    scale. Frequently the scores on these five dimensions are converted to a 
    single utility index using country specific value sets, which can be used
    in the clinical and economic evaluation of health care as well as in 
    population health surveys. The eq5d package provides methods to calculate 
    index scores from a subject's dimension scores. 30 TTO and 11 VAS EQ-5D-3L
    value sets including those for countries in Szende et al (2007) 
    <doi:10.1007/1-4020-5511-0> and Szende et al (2014) 
    <doi:10.1007/978-94-007-7596-1>, 40 EQ-5D-5L EQ-VT value sets, the 
    EQ-5D-5L crosswalk value sets developed by van Hout et al. (2012) 
    <doi:10.1016/j.jval.2012.02.008>, the crosswalk value set for Russia and 
    reverse crosswalk value sets. Nine EQ-5D-Y value sets are also included 
    as are the NICE 'DSU' age-sex based EQ-5D-3L to EQ-5D-5L and EQ-5D-5L to 
    EQ-5D-3L mappings. Methods are also included for the analysis of EQ-5D 
    profiles along with a shiny web tool to enable the calculation, 
    visualisation and automated statistical analysis of EQ-5D data via a web 
    browser using EQ-5D dimension scores stored in CSV or Excel files. 
	"""
	
	homepage = "https://github.com/fragla/eq5d"
	cran = "eq5d" 

	version("0.15.2", md5="42ca443dc45825c6d14fe2605ae03e5c")

	depends_on("r@3.5:", type=("build", "run"))
