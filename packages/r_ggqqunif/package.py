# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgqqunif(RPackage):
	"""Compare Big Datasets to the Uniform Distribution

	A quantile-quantile plot can be used to compare a sample of p-values 
  to the uniform distribution.  But when the dataset is big (i.e. > 1e4 p-values),
  plotting the quantile-quantile plot can be slow.  geom_QQ uses all the data to
  calculate the quantiles, but thins it out in a way that focuses on points near zero 
  before plotting to speed up plotting and decrease file size, when vector graphics are stored.  
	"""
	
	cran = "ggQQunif" 

	version("0.1.5", md5="82e59909281555ed282ed33b738530f8")

	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
