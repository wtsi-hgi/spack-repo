# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastgsdata(RPackage):
	"""Yeast Gold Standard Data

	A collection of so-called gold (and other) standard data sets
	"""
	
	bioc = "yeastGSData"

	version("0.46.0", commit="10ec2b76145ad725a7b6b2d81cd6f567227a553f")
	version("0.40.0", commit="748ef20b868cc075342bd9ca06033ac25a25bdbd")


