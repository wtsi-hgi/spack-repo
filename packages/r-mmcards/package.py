# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmcards(RPackage):
	"""Playing Cards Utility Functions

	Early insights in probability theory were largely influenced by
    questions about gambling and games of chance, as noted by Blitzstein and
    Hwang (2019, ISBN:978-1138369917). In modern times, playing cards continue
    to serve as an effective teaching tool for probability, statistics, and even
    'R' programming, as demonstrated by Grolemund (2014, ISBN:978-1449359010).
    The 'mmcards' package offers a collection of utility functions designed to
    aid in the creation, manipulation, and utilization of playing card decks in
    multiple formats. These include a standard 52-card deck, as well as
    alternative decks such as decks defined by custom anonymous functions and
    custom interleaved decks. Optimized for the development of educational
    'shiny' applications, the package is particularly useful for teaching
    statistics and probability through card-based games. Functions include
    shuffle_deck(), which creates either a shuffled standard deck or a shuffled
    custom alternative deck; deal_card(), which takes a deck and returns a list
    object containing both the dealt card and the updated deck; and i_deck(),
    which adds image paths to card objects, further enriching the package's
    utility in the development of interactive 'shiny' application card games.
	"""
	
	homepage = "https://github.com/mightymetrika/mmcards"
	cran = "mmcards" 

	version("0.1.1", md5="e89d3ab55efa6c6b12e2e20a3dd2d477")

	depends_on("r@2.10:", type=("build", "run"))
