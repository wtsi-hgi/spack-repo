# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCluster(RPackage):
	""" "Finding Groups in Data": Cluster Analysis Extended Rousseeuw et al.

	Methods for Cluster analysis. Much extended the original from Peter
	Rousseeuw, Anja Struyf and Mia Hubert, based on Kaufman and Rousseeuw
	(1990) "Finding Groups in Data"."""

	cran = "cluster"

	version("2.1.6", md5="efd3ba0d58a6dd575b977c84086eb86a")

	depends_on("r@3.5:", type=("build", "run"))
