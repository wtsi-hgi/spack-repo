# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaeg1acdf(RPackage):
	"""paeg1acdf

	A package containing an environment representing the Pae_G1a.CDF file.
	"""
	
	bioc = "paeg1acdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/paeg1acdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/paeg1acdf/paeg1acdf_2.18.0.tar.gz"]

	version("2.18.0", md5="73af974112051db0f715518393e84726")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation