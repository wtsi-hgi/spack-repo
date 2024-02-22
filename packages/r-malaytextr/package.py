# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMalaytextr(RPackage):
	"""Text Mining for Bahasa Malaysia

	It is designed to work with text written in Bahasa Malaysia. We provide 
    functions and data sets that will make working with Bahasa Malaysia text much easier. 
    For word stemming in particular, we will look up the Malay words in a dictionary and
    then proceed to remove "extra suffix" as explained in Khan, Rehman Ullah, 
    Fitri Suraya Mohamad, Muh Inam UlHaq, Shahren Ahmad Zadi Adruce, 
    Philip Nuli Anding, Sajjad Nawaz Khan, and Abdulrazak Yahya Saleh Al-Hababi
    (2017) <https://ijrest.net/vol-4-issue-12.html> . This package includes
    a dictionary of Malay words that may be used to perform word stemming, 
    a dataset of Malay stop words, a dataset of sentiment words
    and a dataset of normalized words.
	"""
	
	homepage = "https://github.com/zahiernasrudin/malaytextr"
	cran = "malaytextr" 

	version("0.1.3", md5="5aac16e70ee88154eb4bef4145df497f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
