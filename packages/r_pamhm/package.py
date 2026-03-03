# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPamhm(RPackage):
	"""Generate Heatmaps Based on Partitioning Around Medoids (PAM)

	Data are partitioned (clustered) into k clusters "around medoids", which is
    a more robust version of K-means implemented in the function pam() in the 'cluster' package.
    The PAM algorithm is described in Kaufman and Rousseeuw (1990) <doi:10.1002/9780470316801>.
    Please refer to the pam() function documentation for more references.
    Clustered data is plotted as a split heatmap allowing visualisation of representative
    "group-clusters" (medoids) in the data as separated fractions of the graph while those
    "sub-clusters" are visualised as a traditional heatmap based on hierarchical clustering.
	"""
	
	cran = "PAMhm" 

	version("0.1.2", md5="d625b0981db049659503f07ee1323ea9")

	depends_on("r-heatmapflex", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-readmore", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-robusthd", type=("build", "run"))
