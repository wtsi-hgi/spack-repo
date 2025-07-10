# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHugene10stv1cdf(RPackage):
	"""hugene10stv1cdf

	A package containing an environment representing the HuGene-1_0-st-v1.cdf file.
	"""
	
	bioc = "hugene10stv1cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hugene10stv1cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hugene10stv1cdf/hugene10stv1cdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="4e7489abd0e678d6cf9cc60f7da068198b47830aade3602af9840cc732653ab7")

	depends_on("r-annotationdbi", type=("build", "run"))

