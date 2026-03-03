# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabr(RPackage):
	"""Music Notation Syntax, Manipulation, Analysis and Transcription
in R

	Provides a music notation syntax and a collection of music 
    programming functions for generating, manipulating, organizing, and analyzing 
    musical information in R. Music syntax can be entered directly in character 
    strings, for example to quickly transcribe short pieces of music. The 
    package contains functions for directly performing various mathematical, 
    logical and organizational operations and musical transformations on special 
    object classes that facilitate working with music data and notation. The 
    same music data can be organized in tidy data frames for a familiar and 
    powerful approach to the analysis of large amounts of structured music data. 
    Functions are available for mapping seamlessly between these formats and 
    their representations of musical information. The package also provides an 
    API to 'LilyPond' (<https://lilypond.org/>) for transcribing musical 
    representations in R into tablature ("tabs") and sheet music. 'LilyPond' is 
    open source music engraving software for generating high quality sheet music 
    based on markup syntax. The package generates 'LilyPond' files from R code 
    and can pass them to the 'LilyPond' command line interface to be rendered 
    into sheet music PDF files or inserted into R markdown documents. The 
    package offers nominal MIDI file output support in conjunction with
    rendering sheet music. The package can read MIDI files and attempts to
    structure the MIDI data to integrate as best as possible with the data
    structures and functionality found throughout the package.
	"""
	
	homepage = "https://github.com/leonawicz/tabr"
	cran = "tabr" 

	version("0.4.9", md5="4b9cc3abea22565127c0a05aae0110e6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
