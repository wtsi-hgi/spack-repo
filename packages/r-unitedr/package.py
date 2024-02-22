# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnitedr(RPackage):
	"""Assessment and Evaluation of Formations in United

	United is a software tool which can be downloaded at the following
    website <http://www.schroepl.net/pbm/software/united/>. In general, it is
    a virtual manager game for football teams. This package contains helpful
    functions for determining an optimal formation for a virtual match in
    United. E.g. knowing that the opponent has a strong defensive it is
    advisable to beat him in the midfield. Furthermore, this package contains
    functions for computing the optimal usage of hardness in a game.
	"""
	
	cran = "unitedR" 

	version("0.4", md5="e1304b10bd8b123d0bf8764184b9ffc2")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
