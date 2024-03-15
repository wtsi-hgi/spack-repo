# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagene10stv1cdf(RPackage):
	"""ragene10stv1cdf

	A package containing an environment representing the RaGene-1_0-st-v1.cdf file.
	"""
	
	bioc = "ragene10stv1cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ragene10stv1cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ragene10stv1cdf/ragene10stv1cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="df696e9dbf5b3f2761b6a0a5914be058")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation