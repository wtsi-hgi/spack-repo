# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastlink(RPackage):
	"""Fast Probabilistic Record Linkage with Missing Data

	Implements a Fellegi-Sunter probabilistic record linkage model that allows for missing data
    and the inclusion of auxiliary information. This includes functionalities to conduct a merge of two 
    datasets under the Fellegi-Sunter model using the Expectation-Maximization algorithm. In addition, 
    tools for preparing, adjusting, and summarizing data merges are included. The package implements methods 
    described in Enamorado, Fifield, and Imai (2019) ''Using a Probabilistic Model to Assist Merging of 
    Large-scale Administrative Records'' <doi:10.1017/S0003055418000783> and is available 
    at <https://imai.fas.harvard.edu/research/linkage.html>.
	"""
	
	cran = "fastLink" 

	version("0.6.1", md5="5bb74a18f8b582aa0ed024a934bacf76")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-adagio", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
