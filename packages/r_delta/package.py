# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDelta(RPackage):
	"""Measure of Agreement Between Two Raters

	Measure of agreement delta was originally by Martín & Femia (2004) <DOI:10.1348/000711004849268>. 
    Since then has been considered as agreement measure for different 
    fields, since their behavior is usually better than the usual kappa index
    by Cohen (1960) <DOI:10.1177/001316446002000104>. The main issue with delta 
    is that can not be computed by hand contrary to kappa. The current algorithm
    is based on the Version 5 of the delta windows program that can be found on
    <https://www.ugr.es/~bioest/software/delta/cmd.php?seccion=downloads>.
	"""
	
	cran = "Delta" 

	version("0.2.0.3", md5="c654a5c145fb35f4213d1c25981b3c57")

	depends_on("r@3.2:", type=("build", "run"))
