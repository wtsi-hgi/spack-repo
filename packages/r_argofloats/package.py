# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArgofloats(RPackage):
	"""Analysis of Oceanographic Argo Floats

	Supports the analysis of oceanographic data recorded by Argo autonomous drifting profiling floats. Functions are provided to (a) download and cache data files, (b) subset data in various ways, (c) handle quality-control flags and (d) plot the results according to oceanographic conventions. A shiny app is provided for easy exploration of datasets. The package is designed to work well with the 'oce' package, providing a wide range of processing capabilities that are particular to oceanographic analysis. See Kelley, Harbin, and Richards (2021) <doi:10.3389/fmars.2021.635922> for more on the scientific context and applications.
	"""
	
	homepage = "https://github.com/ArgoCanada/argoFloats"
	cran = "argoFloats" 

	version("1.0.7", md5="459f42b86a783a09ebb5dc945dfdbcd7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-oce@1.3:", type=("build", "run"))
