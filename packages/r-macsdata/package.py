# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacsdata(RPackage):
	"""Test datasets for the MACSr package

	Test datasets from the MACS3 test examples are use in the examples of the `MACSr` package. All 9 datasets are uploaded to the `ExperimentHub`. The original data can be found at: https://github.com/macs3-project/MACS/.
	"""
	
	bioc = "MACSdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MACSdata_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MACSdata/MACSdata_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="416657b159ac1f4a72546671d21787df759d75e3a54fc6f887e2249bd3f0f284")


