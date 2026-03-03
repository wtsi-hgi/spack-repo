# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustrd(RPackage):
	"""Methods for Joint Dimension Reduction and Clustering

	A class of methods that combine dimension reduction and clustering of continuous, categorical or mixed-type data (Markos, Iodice D'Enza and van de Velden 2019; <DOI:10.18637/jss.v091.i10>). For continuous data, the package contains implementations of factorial K-means (Vichi and Kiers 2001; <DOI:10.1016/S0167-9473(00)00064-5>) and reduced K-means (De Soete and Carroll 1994; <DOI:10.1007/978-3-642-51175-2_24>); both methods that combine principal component analysis with K-means clustering. For categorical data, the package provides MCA K-means (Hwang, Dillon and Takane 2006; <DOI:10.1007/s11336-004-1173-x>), i-FCB (Iodice D'Enza and Palumbo 2013, <DOI:10.1007/s00180-012-0329-x>) and Cluster Correspondence Analysis (van de Velden, Iodice D'Enza and Palumbo 2017; <DOI:10.1007/s11336-016-9514-0>), which combine multiple correspondence analysis with K-means. For mixed-type data, it provides mixed Reduced K-means and mixed Factorial K-means (van de Velden, Iodice D'Enza and Markos 2019; <DOI:10.1002/wics.1456>), which combine PCA for mixed-type data with K-means.
	"""
	
	cran = "clustrd" 

	version("1.4.0", md5="8480bce460d5679c7cabe66c9eb9fcbb")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ca", type=("build", "run"))
