# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcorpora(RPackage):
	"""A Collection of Small Text Corpora of Interesting Data

	A collection of small text corpora of interesting data.
    It contains all data sets from 'dariusk/corpora'. Some examples:
    names of animals: birds, dinosaurs, dogs; foods: beer categories,
    pizza toppings; geography: English towns, rivers, oceans;
    humans: authors, US presidents, occupations; science: elements,
    planets; words: adjectives, verbs, proverbs, US president quotes.
	"""
	
	homepage = "https://github.com/gaborcsardi/rcorpora"
	cran = "rcorpora" 

	version("2.0.0", md5="58dc086bc146edb3074057fac5eea1f7")

	depends_on("r-jsonlite", type=("build", "run"))
