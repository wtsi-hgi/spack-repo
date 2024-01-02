# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RTesseract(RPackage):
    """Bindings to 'Tesseract': a powerful optical character recognition (OCR) engine that supports over 100 languages."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://docs.ropensci.org/tesseract/"
    cran = "tesseract"

    version("5.2.0", sha256="1f85aa03cea8e24822bae34ae7c2a42116fdd3c7713464af3445196f8c2601f2")
    version("5.1.0", sha256="6dae7cbc1d4cf6decabb2d1c56d95b5eb6a0a4a1cbc9f9a1c274ba558b31cdfa")
    version("5.0.0", sha256="96c5688a5945f3fd61816ad12ad702ad568fd00382b2d8242de1d9b84695bcf5")
    version("4.2.0", sha256="2fbc868836027a79f52fa4b99ad55aee320e940f82f85f49c270e8ebc5185a86")
    version("4.1.2", sha256="5042f64f357f9aa4bca8a817a84dea6a2825425e8608d7514fc75838118949f4")
    version("4.1.1", sha256="75bf601815feb8bbdde73f5812280004a99aea0f2bf4a6edc4041e7a41f49ebb")
    version("4.1", sha256="c0754a893352f52db44d47911173e7a64f83217671888f6d34adc1631171eca8")
    version("4.0", sha256="30267d7f41f5ec4ce163796f4d285703538aaa8eb076c0322179a307f0c84db5")
    version("2.3", sha256="c683563943865e0337e1cfd472333c2bd64bc9f92ccf1df43487597301536693")
    version("2.2", sha256="0239fea0d3386b5443e5d6ca2fbbe1ee15d6a69a2374e91c6b481927225da46b")
    version("2.1", sha256="25b421b00544f0e3587427decf57b49e0ab79761e56d5c6c2cbae6a6d3f96487")
    version("2.0", sha256="ce5efa5cc9ec599cb322d446b55a302ed5b7076c758a9794dba5e713a545fa36")
    version("1.9", sha256="f1eb8480d2d5244cf71f2c9e39ab1dee76b02582c94a27caf7e8db8e34823853")
    version("1.8", sha256="149b53291a2507e4fcca542f7495a367eaecc1766dfc5c59e35f2aba98a15591")
    version("1.6", sha256="2b23d7cadd7aa470db02b9615ca7bd04101617d486f034986c2cfb95e7aaecaa")
    version("1.4", sha256="27eedb0ddeaa1671f2724ccf1dc1ece77ea6bcbd200d585be677494b366599f9")
    version("1.3", sha256="446786c11d378ae8c075b371b5ab0a6fd3e69c36d6e669e146138b96491d339f")
    version("1.2", sha256="9fe61761b02ae3ee93c94efaa61d2d385c484c998bc9e380ee30324999b4de2d")
    version("1.1", sha256="a0e8d08a4ba0797de3aa1676b911948618ad6e399c1cca7a7235b5a7566f7bf3")
    version("1.0", sha256="4b7c497b7ab6eca2d4be976ff8af39bbf0e201b173f5164da083d88cc723f08f")

    depends_on("r-rcpp@0.12.12:", type=("build", "run"))
    depends_on("r-pdftools@1.5:", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-rappdirs", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-magick@1.7:", type=("build", "run"))
    depends_on("r-spelling", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("tesseract", type=("build", "run"))
