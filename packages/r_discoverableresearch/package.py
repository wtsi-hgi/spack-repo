# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscoverableresearch(RPackage):
	"""Checks Title, Abstract and Keywords to Optimise Discoverability

	A suite of tools are provided here to support authors in making their research more discoverable. 
    check_keywords() - this function checks the keywords to assess whether they are already represented in the 
    title and abstract. check_fields() - this function compares terminology used across the title, abstract 
    and keywords to assess where terminological diversity (i.e. the use of synonyms) could increase the likelihood 
    of the record being identified in a search. The function looks for terms in the title and abstract that also 
    exist in other fields and highlights these as needing attention. suggest_keywords() - this function takes a 
    full text document and produces a list of unigrams, bigrams and trigrams (1-, 2- or 2-word phrases) 
    present in the full text after removing stop words (words with a low utility in natural language processing) 
    that do not occur in the title or abstract that may be suitable candidates for keywords. suggest_title() - 
    this function takes a full text document and produces a list of the most frequently used unigrams, bigrams 
    and trigrams after removing stop words that do not occur in the abstract or keywords that may be suitable 
    candidates for title words. check_title() - this function carries out a number of sub tasks:  1) it compares 
    the length (number of words) of the title with the mean length of titles in major bibliographic databases to 
    assess whether the title is likely to be too short; 2) it assesses the proportion of stop words in the title 
    to highlight titles with low utility in search engines that strip out stop words; 3) it compares the title 
    with a given sample of record titles from an .ris import and calculates a similarity score based on phrase 
    overlap. This highlights the level of uniqueness of the title. This version of the package also contains 
    functions currently in a non-CRAN package called 'litsearchr' <https://github.com/elizagrames/litsearchr>.
	"""
	
	cran = "discoverableresearch" 

	version("0.0.1", md5="afe1fda45775a5fea595ccd1fb405232")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ngram", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stopwords", type=("build", "run"))
	depends_on("r-synthesisr", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
