# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhesuscdf(RPackage):
	"""rhesuscdf

	A package containing an environment representing the Rhesus.cdf file.
	"""
	
	bioc = "rhesuscdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/rhesuscdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/rhesuscdf/rhesuscdf_2.18.0.tar.gz"]

	version("2.18.0", md5="994e16da5dd31bc2796d0da40aa2634f")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation