# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustBinPair(RPackage):
	"""Statistical Methods for Analyzing Clustered Matched Pair Data

	Tests, utilities, and case studies for analyzing significance in
  clustered binary matched-pair data. The central function clust.bin.pair uses
  one of several tests to calculate a Chi-square statistic. Implemented are the
  tests Eliasziw (1991) <doi:10.1002/sim.4780101211>, Obuchowski (1998)
  <doi:10.1002/(SICI)1097-0258(19980715)17:13%3C1495::AID-SIM863%3E3.0.CO;2-I>,
  Durkalski (2003) <doi:10.1002/sim.1438>, and Yang (2010)
  <doi:10.1002/bimj.201000035> with McNemar (1947) <doi:10.1007/BF02295996>
  included for comparison. The utility functions nested.to.contingency and
  paired.to.contingency convert data between various useful formats. Thyroids
  and psychiatry are the canonical datasets from Obuchowski and Petryshen (1989)
  <doi:10.1016/0165-1781(89)90196-0> respectively.
	"""
	
	homepage = "https://github.com/dgopstein/clust.bin.pair"
	cran = "clust.bin.pair" 

	version("0.1.2", md5="ea257c948af2f4bbfe9ca3317b406ee6")

	depends_on("r@3.2.4:", type=("build", "run"))
