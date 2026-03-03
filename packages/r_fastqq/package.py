# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastqq(RPackage):
	"""Faster Generation of Quantile Quantile Plots with Large Samples

	New and faster implementations for quantile quantile plots. 
    The package also includes a function to prune data for quantile quantile 
    plots. This can drastically reduce the running time for large samples, 
    for 100 million samples, you can expect a factor 80X speedup.
	"""
	
	homepage = "https://github.com/gumeo/fastqq"
	cran = "fastqq" 

	version("0.1.3", md5="a00f34f3d12dd4224c63224756f42453")

	depends_on("r-rcpp", type=("build", "run"))
