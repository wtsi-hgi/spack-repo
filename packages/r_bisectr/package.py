# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBisectr(RPackage):
	"""Tools to find bad commits with git bisect

	Tools to find bad commits with git bisect. See
        https://github.com/wch/bisectr for examples and test script
        templates.
	"""
	
	homepage = "https://github.com/wch/bisectr"
	cran = "bisectr" 

	version("0.1.0", md5="ec32666f66f64fccc5d8f262f33e2f1b")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
