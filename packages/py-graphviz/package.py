# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyGraphviz(PythonPackage):
    """Simple Python interface for Graphviz"""

    homepage = "https://github.com/xflr6/graphviz"
    pypi = "graphviz/graphviz-0.10.1.zip"

    license("MIT")

    version("0.20.3", sha256="09d6bc81e6a9fa392e7ba52135a9d49f1ed62526f96499325930e87ca1b5925d")
    version("0.20.2", sha256="d29ca3aadbe5d6e6c584045b7ec4fc1c15af2448dc1c0211b5e94344833243da")
    version("0.20.1", sha256="8c58f14adaa3b947daf26c19bc1e98c4e0702cdc31cf99153e6f06904d492bf8")
    version("0.20", sha256="76bdfb73f42e72564ffe9c7299482f9d72f8e6cb8d54bce7b48ab323755e9ba5")
    version("0.19.2", sha256="7c90cebc147c18bcdffcd3c76db58cbface5d45fe0247a2f3bfb144d32a8c77c")
    version("0.19.1", sha256="09ed0cde452d015fe77c4845a210eb642f28d245f5bc250d4b97808cb8f49078")
    version("0.19", sha256="b42554a1c47f24a9473b7f4e380d17b228586a067c97ea69d5354d6074be8dfd")
    version("0.18.2", sha256="b876ad68bc7b441f05dee6b36cc338c6b95ddb4e523bb7313c9f3dfe56fc342a")
    version("0.18.1", sha256="bb78fbd032590dbfbbb56805b39d61fd5225d165bbf03de1e46873eec48f4b8f")
    version("0.18", sha256="0f04e5f939d3a839b524283d590e941892c56e75e60e0f5238c431264f490022")
    version("0.17", sha256="ef6e2c5deb9cdcc0c7eece1d89625fd07b0f2208ea2bcb483520907ddf8b4e12")
    version("0.16", sha256="d2d25af1c199cad567ce4806f0449cb74eb30cf451fd7597251e1da099ac6e57")
    version("0.15", sha256="2b85f105024e229ec330fe5067abbe9aa0d7708921a585ecc2bf56000bf5e027")
    version("0.14.2", sha256="92b7637ece63c77e3d39221ae1f4df98e9256cb449e9860c598335b34496d195")
    version("0.14.1", sha256="f5aad52a652c06825dcc5ee018d920fca26aef339386866094597fb3f2f222ce")
    version("0.14", sha256="e104ba036c8aef84320ec80560e544cd3cad68c9f90394b4e2b87bc44ab09791")
    version("0.13.2", sha256="60acbeee346e8c14555821eab57dbf68a169e6c10bce40e83c1bf44f63a62a01")
    version("0.13", sha256="dc08677f37c65a4a480f00df4bd0d19a0a103c06aad95f21a37f0b7fd440de81")
    version("0.12", sha256="c60e232a66e4847f9f644fbaa94730ca4f78385a1314a2cc1e7f4cb2d7461298")
    version("0.11.1", sha256="914b8b124942d82e3e1dcef499c9fe77c10acd3d18a1cfeeb2b9de05f6d24805")
    version("0.10.1", sha256="d311be4fddfe832a56986ac5e1d6e8715d7fcb0208560da79d1bb0f72abef41f")
    version("0.8.4", sha256="4958a19cbd8461757a08db308a4a15c3d586660417e1e364f0107d2fe481689f")

    variant("dev", default=False, description="development mode")
    variant("docs", default=False, description="build documentation")

    depends_on("python@2.7:2.8,3.4:", type=("build", "run"), when="@:0.10.1")
    depends_on("python@2.7:2.8,3.5:", type=("build", "run"), when="@0.11.0:")
    depends_on("py-setuptools", type="build")
    depends_on("py-tox@3.0:", type=("build", "run"), when="+dev")
    depends_on("py-flake8", type=("build", "run"), when="+dev")
    depends_on("py-pep8-naming", type=("build", "run"), when="+dev")
    depends_on("py-wheel", type=("build", "run"), when="+dev")
    depends_on("py-twine", type=("build", "run"), when="+dev")
    depends_on("py-sphinx@1.7:", type=("build", "run"), when="+docs")
    depends_on("py-sphinx-rtd-theme", type=("build", "run"), when="+docs")
