# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlimatestingdata(RPackage):
	"""Data for testing of the package blima.

	Experiment data package. The set were prepared using microarray images of human mesenchymal cells treated with various supplements. This package is intended to provide example data to test functionality provided by blima.
	"""
	
	homepage = "https://bitbucket.org/kulvait/blima"
	bioc = "blimaTestingData"

	version("1.28.0", commit="11070cece70c0a164428599cc09d443c08979072")
	version("1.22.0", commit="f167f7fd8c85374f0e3186e73bbba2ab1ed65c7d")

	depends_on("r@3:", type=("build", "run"))

