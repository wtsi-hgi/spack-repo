# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathnetdata(RPackage):
	"""Experimental data for the PathNet package

	This package contains the data employed in the vignette of the PathNet package. These data belong to the following publication: PathNet: A tool for pathway analysis using topological information. Dutta B, Wallqvist A, and Reifman J., Source Code for Biology and Medicine 2012 Sep 24;7(1):10.
	"""
	
	bioc = "PathNetData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/PathNetData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/PathNetData/PathNetData_1.38.0.tar.gz"]

	version("1.38.0", sha256="7880d5e2d2ee60353b1dc089395b366f6293e7fd80e22ca6af3fc3684431981f")

	depends_on("r@1.14:", type=("build", "run"))

