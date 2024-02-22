# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcce(RPackage):
	"""Translate English Words into Chinese, or Translate Chinese Words
into English

	If translate English words into Chinese, there is a faster 
    way for R user. 'RYoudaoTranslate' package provides interface to 
    'Youdao' <http://youdao.com/> translation open API for R user. 'entcn' 
    package also provides similar features. But it does not support Chinese 
    words translation into English, I have made some improvements on the basis 
    of this software. You can pass in an English or Chinese word, ecce package 
    support both English and Chinese translation. It also support browse 
    translation results in website. In addition, also support obtain the pinyin 
    of the Chinese character, so that you can more easily understand the 
    pronunciation of the Chinese character.
	"""
	
	homepage = "https://cxy.rbind.io/ecce/"
	cran = "ecce" 

	version("2.0.6", md5="9dbb41ab58b42229e846afb6985e7e2e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
