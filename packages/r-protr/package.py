# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProtr(RPackage):
	"""Generating Various Numerical Representation Schemes for Protein
Sequences

	Comprehensive toolkit for generating various numerical
    features of protein sequences described in Xiao et al. (2015)
    <DOI:10.1093/bioinformatics/btv042>. For full functionality,
    the software 'ncbi-blast+' is needed, see
    <https://blast.ncbi.nlm.nih.gov/doc/blast-help/downloadblastdata.html>
    for more information.
	"""
	
	homepage = "https://nanx.me/protr/"
	cran = "protr" 

	version("1.7-0", md5="e13e53d13fd27b7e4718a32df6ceeac5")

	depends_on("r@3.0.2:", type=("build", "run"))
