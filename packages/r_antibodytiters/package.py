# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAntibodytiters(RPackage):
	"""Antibody Titer Analysis of Vaccinated Patients

	Visualization of antibody titer scores is valuable for examination of vaccination 
    effects. 'AntibodyTiters' visualizes antibody titers of all or selected patients. This 
    package also produces empty excel files in a specified format, in which users can fill in 
    experimental data for visualization. Excel files with toy data can also be produced, so that 
    users can see how it is visualized before obtaining real data. The data should contain 
    titer scores at pre-vaccination, after-1st shot, after-2nd shot, and at least one 
    additional sampling points. Patients with missing values can be included. The first two 
    sampling points (pre-vaccination and after-1st shot) will be plotted discretely, whereas 
    those following will be plotted on a continuous time scale that starts from the day of 
    second shot. Half-life of titer can also be calculated for each pair of sampling points.
	"""
	
	cran = "AntibodyTiters" 

	version("0.1.24", md5="8a5f54f70a0d5971cec60b0ef902c1e5")

	depends_on("r-openxlsx@4.2.4:", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-desctools@0.99.43:", type=("build", "run"))
