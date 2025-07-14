# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRitandata(RPackage):
	"""This package contains reference annotation and network data sets

	Data such as is contained in the two R data files in this package are required for the RITAN package examples. Users are highly encouraged to use their own or additional resources in conjunction with RITANdata. See the RITAN vignettes and RITAN.md for more information, such as gathering more up-to-date annotation data.
	"""
	
	bioc = "RITANdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RITANdata_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RITANdata/RITANdata_1.26.0.tar.gz"]

    version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="42bfcad2eac4d5fbf54dd8e5dbbb5430613ca2cd962f8f36e87719281e716c4a")

	depends_on("r@4.2:", type=("build", "run"))

