# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdspatialscan(RPackage):
	"""Multivariate and Functional Spatial Scan Statistics

	Allows to detect spatial clusters of abnormal values on multivariate or functional data. Martin KULLDORFF and Lan HUANG and Kevin KONTY (2009) <doi:10.1186/1476-072X-8-58>, Inkyung JUNG and Ho Jin CHO (2015) <doi:10.1186/s12942-015-0024-6>, Lionel CUCALA and Michael GENIN and Caroline LANIER and Florent OCCELLI (2017) <doi:10.1016/j.spasta.2017.06.001>, Lionel CUCALA and Michael GENIN and Florent OCCELLI and Julien SOULA (2019) <doi:10.1016/j.spasta.2018.10.002>, Camille FREVENT and Mohamed-Salem AHMED and Matthieu MARBAC and Michael GENIN (2021) <doi:10.1016/j.spasta.2021.100550>, Zaineb SMIDA and Lionel CUCALA and Ali GANNOUN and Ghislain Durif (2022) <doi:10.1016/j.csda.2021.107378>, Camille FREVENT and Mohamed-Salem AHMED and Sophie DABO-NIANG and Michael GENIN (2023) <doi:10.1093/jrsssc/qlad017>.
	"""
	
	cran = "HDSpatialScan" 

	version("1.0.4", md5="7f90cce2f78fd4a778aedde818f2e473")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-spatialnp", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-swfscmisc", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
