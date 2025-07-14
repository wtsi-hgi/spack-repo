# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialdmelxsim(RPackage):
	"""Spatial allelic expression counts for fly cross embryo

	Spatial allelic expression counts from Combs & Fraser (2018), compiled into a SummarizedExperiment object. This package contains data of allelic expression counts of spatial slices of a fly embryo, a Drosophila melanogaster x Drosophila simulans cross. See the CITATION file for the data source, and the associated script for how the object was constructed from publicly available data.
	"""
	
	homepage = "https://github.com/mikelove/spatialDmelxsim"
	bioc = "spatialDmelxsim"

	version("1.14.0", commit="381ea05157ad185a5a8f46321da43897a5997465")
	version("1.8.0", commit="13717a1f4a018a61b82824f8457a73a2cc1e547e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

