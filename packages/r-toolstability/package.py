# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToolstability(RPackage):
	"""Tool for Stability Indices Calculation

	Tools to calculate stability indices with parametric,
 non-parametric and probabilistic approaches. The basic data format requirement for 'toolStability' is a data frame with 3 columns including numeric trait values, genotype,and environmental labels. Output format of each function is the dataframe with chosen stability index for each genotype. 
 Function "table_stability" offers the summary table of all stability indices in this package. 
 This R package toolStability is part of the main publication: 
 Wang, Casadebaig and Chen (2023) <doi:10.1007/s00122-023-04264-7>. 
 Analysis pipeline for main publication can be found on github: <https://github.com/Illustratien/Wang_2023_TAAG/tree/V1.0.0>. 
 Sample dataset in this package is derived from another publication:  
 Casadebaig P, Zheng B, Chapman S et al. (2016) <doi:10.1371/journal.pone.0146385>. 
 For detailed documentation of dataset, please see on Zenodo <doi:10.5281/zenodo.4729636>. 
 Indices used in this package are from: 
 Döring TF, Reckling M (2018) <doi:10.1016/j.eja.2018.06.007>. 
 Eberhart SA, Russell WA (1966) <doi:10.2135/cropsci1966.0011183X000600010011x>. 
 Eskridge KM (1990) <doi:10.2135/cropsci1990.0011183X003000020025x>. 
 Finlay KW, Wilkinson GN (1963) <doi:10.1071/AR9630742>. 
 Hanson WD (1970) Genotypic stability. <doi:10.1007/BF00285245>. 
 Lin CS, Binns MR (1988) <https://cdnsciencepub.com/doi/abs/10.4141/cjps88-018>. 
 Nassar R, Hühn M (1987). 
 Pinthus MJ (1973) <doi:10.1007/BF00021563>. 
 Römer T (1917). 
 Shukla GK (1972). 
 Wricke G (1962). 
	"""
	
	homepage = "https://illustratien.github.io/toolStability/"
	cran = "toolStability" 

	version("0.1.2", md5="a3f648372a7f8df587c1a559db60c1a8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
