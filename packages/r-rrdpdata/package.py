# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrdpdata(RPackage):
	"""Database for the Default RDP Classifier

	Database used by the default RDP Classifier
	"""
	
	bioc = "rRDPData"

	version("1.28.0", commit="b06d16c7467e5692b37b7717d1917bb3adb890ae")
	version("1.22.0", commit="1b0000d5f65e2f128b946d96cae342bb2be6c336")

	depends_on("r-rrdp", type=("build", "run"))
	depends_on("openjdk", type=("build", "link", "run"))

