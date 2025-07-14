# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowfp(RPackage):
	"""Fingerprinting for Flow Cytometry

	Fingerprint generation of flow cytometry data, used to facilitate the application of machine learning and datamining tools for flow cytometry.
	"""
	
	bioc = "flowFP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowFP_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowFP/flowFP_1.60.0.tar.gz"]

    version("1.66.0", tag="RELEASE_3_21")
	version("1.60.0", sha256="f58cf1d0947a64f04a101b74eedead6dc441d465c6cf4abad1a8831e4711d834")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowviz", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics@0.1.6:", type=("build", "run"))
