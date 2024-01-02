# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RPdftools(RPackage):
    """Utilities based on 'libpoppler' for extracting text, fonts, attachments and metadata from a PDF file."""

    homepage = "https://docs.ropensci.org/pdftools/"
    cran = "pdftools"

    version("3.4.0", sha256="0b9d7b2100a6d7959c56e144285b9638ca6ff4a7f484a31ff814a99d71482c64")
    version("3.3.3", sha256="ffc0dfa5205ac3c26ee22713289784cb6b9aada6c21417d79bfd4d7f5bd5909c")
    version("3.3.2", sha256="451f4ad7699d482eaf847684ea0f384049cbb3b7a22ff89a02b30e091f4a5a04")
    version("3.3.1", sha256="96b999b99c05175c6a32e253d9bf5080ff45a5e92b6509cdd6d15b6d7ade3fe2")
    version("3.3.0", sha256="0913d2eae9718b11245a9b3d970b11152afbc83ee1424cd4e42f76fbd53e2e94")
    version("3.2.1", sha256="d1e18f7c9366e7613f61c0266c584412c8e448cfc1f71101b5c8d1dd6cbb37ad")
    version("3.2.0", sha256="a2ae003d730cfdd95dbd3a7eecbd8ce4ecd3cb43441700e6bfa5d897e714982c")
    version("3.1.1", sha256="2651283b68826ed8dc73f33b41ae268332e4759d5efa3d06e0a4b6eb85c3d4d1")
    version("3.1.0", sha256="514532d9ede84d90ba584371c648f7adca77380b4532a1170f250cd076e45618")
    version("3.0.1", sha256="13d5935459aef1ea0ad215f5004696754e3463aa2191eed73af1235f6cd18bb5")
    version("3.0.0", sha256="b2015dd4bd47423af17d73a32b6ab497ebbaf9c551de6e2a7e1f51b55e2f692c")
    version("2.3.1", sha256="5d373b46acc226f7dfe41f0617876d84fe394fdc999e4a3fd011ea29ab782506")
    version("2.3", sha256="c9c45206bb7ed3d684147ff474c1b23d7283a655dc24cb9c9af94548ce1e29ec")
    version("2.2", sha256="14cccc891a0a491ab8be6709620918aa9319415be8016c4e3b39812ec7c875b3")
    version("2.1", sha256="5b892bac7f37f80955d2c1ede600876be055e2619f2a76009197ae8e5ea5ce70")
    version("2.0", sha256="58e9739b435e1d9e2e8fce6f31d338853255537f575d7674207039a4e2d90aa2")
    version("1.8", sha256="5f790c3678eacdc15147a671571c86b5f8d6eb692fa680324bc5d27542e6d0fb")
    version("1.7", sha256="8fa927d73a357503221017d9abaca536496c0df187262f733c954c762b208767")
    version("1.6", sha256="9b950be97beb27a490be065aade8dcb2672d70ccc83b497960fbcb596ce8a502")
    version("1.5", sha256="9a9e87beb36a42d0ebc5c51af6107978ea5f69efbe747e67fb16dcf5c909e427")
    version("1.4", sha256="76b09ce8bc290601399f20258312076b9d75edf749d3ba353bc54a167003a962")
    version("1.3", sha256="1f9a5c9b5cedfb6ee45db545f260e79533fbbe0734b99b086fd194ed7a284e3d")
    version("1.2", sha256="06fa3986e3bc43914e56883f53a009f79790f68b78ace6a9ee227af17106bcb9")
    version("1.1", sha256="61b62f1bccfbd113cbc2e1f3173f8d328579b732f0f8cf42b6197e0bda7c6084")
    version("1.0", sha256="2517a6add67deda96d3906ac04fa864cc42140c709ac6374106f4cfef7a62efe")
    version("0.5", sha256="779a4b54c24f0ded8a7f7c42ab6a9371025a8fc6e27b831a08876cbaa3ddd5f5")
    version("0.4", sha256="e16c7f10b8e3e4627a8f610e89161063dab530e954a8600455c1f61349aea577")
    version("0.3", sha256="9e9ceb3dd2f8e613c4c040eafc4ebd38ce524b33663597c034086c8361969a73")
    version("0.2", sha256="6dd227d13034bfb5b034a3da29d2d0b42c77f41957b2ac89e42ba2fe5078437b")
    version("0.1", sha256="8ec876c5e284286d39354ded39193a999d99d5b4030774e387b1242b6cf37d26")

    depends_on("r-rcpp@0.12.12:", type=("build", "run"))
    depends_on("r-qpdf", type=("build", "run"))
    depends_on("r-png", type=("build", "run"))
    depends_on("r-webp", type=("build", "run"))
    depends_on("r-tesseract", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
