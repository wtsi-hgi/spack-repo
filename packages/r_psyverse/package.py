# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsyverse(RPackage):
	"""Decentralized Unequivocality in Psychological Science

	The constructs used to study the human psychology have
    many definitions and corresponding instructions for eliciting
    and coding qualitative data pertaining to constructs' content and
    for measuring the constructs. This plethora of definitions and
    instructions necessitates unequivocal reference to specific
    definitions and instructions in empirical and secondary research.
    This package implements a human- and machine-readable standard for
    specifying construct definitions and instructions for measurement
    and qualitative research based on 'YAML'. This standard facilitates
    systematic unequivocal reference to specific construct definitions
    and corresponding instructions in a decentralized manner (i.e.
    without requiring central curation; Peters (2020)
    <doi:10.31234/osf.io/xebhn>).
	"""
	
	homepage = "https://psyverse.one"
	cran = "psyverse" 

	version("0.2.6", md5="640cd8e6ff6d4a71839385fb2eeb925c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-yaml@2.1.19:", type=("build", "run"))
	depends_on("r-yum@0.0.1:", type=("build", "run"))
