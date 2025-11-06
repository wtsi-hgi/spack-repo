# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNgsTools(PythonPackage):
    """Reusable tools for working with next-generation sequencing (NGS) data"""
    
    homepage = "https://github.com/Lioscro/ngs-tools"
    pypi = "ngs-tools/ngs_tools-1.8.6-py3-none-any.whl" 

    version("1.1.2", sha256="1655e20b854e794ff6a8f519ed9e892ef24b747ad94e01ae5aa1e2c1f6de6d5d")
    version("1.2.0", sha256="6462ce10eb5bf16c779815c467a6425f85736a7d716d876410efd75de01182fe")
    version("1.2.1", sha256="793467239a91998f30015de6427b4b750e158a9a2e4b081206169c9e861eb39f")
    version("1.2.2", sha256="e20db65e63b6325da0753078b90559bacb31da316412c1f0b8c6122aa0f4e733")
    version("1.2.3", sha256="ddb6022fe8cc2e1e106702f668366fe16b27bc10fee67dfad2808b63baba26ce")
    version("1.3.0", sha256="2afdea16253b5000e7c7fc725819067a069ce9407fda76098fe34d37a2379e74")
    version("1.4.0", sha256="9f6c46a303df58b32b1a73f3d04af7fcf502bf00e569cd457873c777733ddd7e")
    version("1.5.0", sha256="fa3306393abf0e0f335471406d4d77655e0c92fab9ae17d37553704b974474e6")
    version("1.5.1", sha256="aea0cead51f1c5a9a9dedbba253c217d2cf67ff221c44431fcc8115d11d7d207")
    version("1.5.10", sha256="cfc97dc257b2af316de7ab2dd8879bda4557f41d27767e01cf1c480869eec474")
    version("1.5.11", sha256="c95325b001ed790ba49412d3e1cf1a9f36b495bce646096c5698fb91909a7b69")
    version("1.5.12", sha256="bb812dafe08bdb11880131f57ac8d4652c590fff7d3dd800327776495b5a4988")
    version("1.5.13", sha256="22e86a6e7a860be01cff30940d47b22fb3ca77f25e3b7b9a8703590f5c14c2b0")
    version("1.5.14", sha256="dd440d0cfd6a00cbc861bc9196c9ad484e6be7e8e7ca7380ceb412d2fd26ec39")
    version("1.5.2", sha256="d4a384ec37b3c05a30e1213f8cd841f4da024208041ac4aa33c77ef604f39856")
    version("1.5.3", sha256="8d533065ba84ee138ed2f778f6fb328bd24260d5cee191fd801c10e7402349c3")
    version("1.5.4", sha256="573722f9d636232a5a808d0037871c767c1bb3f9e2a2f4746efa906fc66ae5b9")
    version("1.5.5", sha256="62ee9bbdef20906681f0f545c3bbcf17e58bddc20568b431c977d601cb3dfa03")
    version("1.5.6", sha256="5cd8e3f55070829269f9f7c4d018f7d12c4a18a171f608aa284f94b6cf9603a9")
    version("1.5.7", sha256="1e4183a665f576ce553e6a3452b10270a8b1c806ff7d04ff0b1fe31029815e42")
    version("1.5.8", sha256="3ee2eebe1d8809c394f5b7cd89152daaafe779d5472750960932bc35a4f0b9a7")
    version("1.5.9", sha256="ccf4acbc58c8ec99252808571b8cb3de18def0a8da5018696a003f435f1260ab")
    version("1.6.0", sha256="332b5f15badb47ed9aa2df9d443200ee0ec0bab993eb5c4649df2607c1ef60f9")
    version("1.7.0", sha256="d2f9340c6d83ef26f6297a099ad96e2f2128d246a4540680c652f995ff1f90ed")
    version("1.7.1", sha256="65f68195edbb52185d7a0973e718f4b54890837d07efc8f610a9d2cdfbdaa4c2")
    version("1.7.2", sha256="061d222cd5cb23fc974f0f4d89c46b4c500d60cf54d3f1f5c98ef6f2a3550073")
    version("1.7.3", sha256="975de879eeb85236903b5ba4be58671a755229eab7c16473c75ee2b48945efa8")
    version("1.8.0", sha256="2f214e36a5a6bfc6fe5a6d550442a8154f8f346a51a60e3746e5a5ede8ac25bd")
    version("1.8.1", sha256="59d606d6c3ff3024e5e1ccad947c4d7608098fca105762e344742e16aa2f0de3")
    version("1.8.3", sha256="c50e36105654cdea14b4c7971994a3e710157663aaf0fd72c4d83a486f12cdb0")
    version("1.8.4", sha256="8c54fe3f3a85f2c3e9c185e389ac83bb2bb4c76cf2bb1204e90d33d241f91f98")
    version("1.8.5", sha256="e8861d26aee5ab74e1aef8170241b2315fbbe1027a10a89566e536204e2873a5", expand=False, url="https://files.pythonhosted.org/packages/95/55/54b341a41be85d3b602b53db1eb415957b990414236219cafca94349220d/ngs_tools-1.8.5-py3-none-any.whl")
    version("1.8.6", sha256="38aaa475c455c3a05b4ae497d01699ac27a7c2dc43f4f09f061acac106445165", expand=False, url="https://files.pythonhosted.org/packages/f5/f3/5c2cd46509d5f3894d59de7bd72abef4e8cd81b47da4520a76e1ea87e733/ngs_tools-1.8.6-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-shortuuid", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))

# {'joblib>=1.0.1': ['1.8.5'], 'numba>=0.53.1': ['1.8.5'], 'numpy>=1.19.0': ['1.8.5'], 'pysam>=0.16.0.1': ['1.8.5'], 'shortuuid>=1.0.1': ['1.8.5'], 'tqdm>=4.50.0': ['1.8.5'], 'typing-extensions>=3.7.4': ['1.8.5'], "pyseq-align>=1.0.0;extra=='levenshtein'": ['1.8.5'], 'joblib(>=1.0.1)': ['1.8.6'], 'numba(>=0.53.1)': ['1.8.6'], 'numpy(>=1.19.0)': ['1.8.6'], 'pysam(>=0.16.0.1)': ['1.8.6'], 'shortuuid(>=1.0.1)': ['1.8.6'], 'tqdm(>=4.50.0)': ['1.8.6'], 'typing-extensions(>=3.7.4)': ['1.8.6'], "pyseq-align(>=1.0.0);extra=='levenshtein'": ['1.8.6']}