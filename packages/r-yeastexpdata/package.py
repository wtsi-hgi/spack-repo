# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastexpdata(RPackage):
	"""Yeast Experimental Data

	A collection of different sets of experimental data from yeast.
	"""
	
	bioc = "yeastExpData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/yeastExpData_0.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/yeastExpData/yeastExpData_0.48.0.tar.gz"]

	version("0.54.0", tag="RELEASE_3_21")
	version("0.48.0", sha256="da4246b77ee008f993acaf4e688634fd5740a73b80fe9e88c94df2be35cb1d8e")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-graph@1.9.26:", type=("build", "run"))

