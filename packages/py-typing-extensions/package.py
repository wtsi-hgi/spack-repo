# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTypingExtensions(PythonPackage):
    """The typing_extensions module contains both backports of these
    changes as well as experimental types that will eventually be
    added to the typing module, such as Protocol (see PEP 544 for
    details about protocols and static duck typing)."""

    homepage = "https://github.com/python/typing_extensions"
    pypi = "typing_extensions/typing_extensions-3.7.4.tar.gz"

    version("4.14.1", sha256="38b39f4aeeab64884ce9f74c94263ef78f3c22467c8724005483154c26648d36")
    version("4.14.0", sha256="8676b788e32f02ab42d9e7c61324048ae4c6d844a399eebace3d4979d75ceef4")
    version("4.13.2", sha256="e6c81219bd689f51865d9e372991c540bda33a0379d5573cddb9a3a23f7caaef")
    version("4.13.1", sha256="98795af00fb9640edec5b8e31fc647597b4691f099ad75f469a2616be1a76dff")
    version("4.13.0", sha256="0a4ac55a5820789d87e297727d229866c9650f6521b64206413c4fbada24d95b")
    version("4.12.2", sha256="1a7ead55c7e559dd4dee8856e3a88b41225abfe1ce8df57b7c13915fe121ffb8")
    version("4.12.1", sha256="915f5e35ff76f56588223f15fdd5938f9a1cf9195c0de25130c627e4d597f6d1")
    version("4.12.0", sha256="8cbcdc8606ebcb0d95453ad7dc5065e6237b6aa230a31e81d0f440c30fed5fd8")
    version("4.11.0", sha256="83f085bd5ca59c80295fc2a82ab5dac679cbe02b9f33f7d83af68e241bea51b0")
    version("4.10.0", sha256="b0abd7c89e8fb96f98db18d86106ff1d90ab692004eb746cf6eda2682f91b3cb")
    version("4.8.0", sha256="df8e4339e9cb77357558cbdbceca33c303714cf861d1eef15e1070055ae8b7ef")
    version("4.6.3", sha256="d91d5919357fe7f681a9f2b5b4cb2a5f1ef0a1e9f59c4d8ff0d3491e05c0ffd5")
    version("4.5.0", sha256="5cb5f4a79139d699607b3ef622a1dedafa84e115ab0024e0d9c044a9479ca7cb")
    version("4.3.0", sha256="e6d2677a32f47fc7eb2795db1dd15c1f34eff616bcaf2cfb5e997f854fa1c4a6")
    version("4.2.0", sha256="f1c24655a0da0d1b67f07e17a5e6b2a105894e6824b92096378bb3668ef02376")
    version("4.1.1", sha256="1a9462dcc3347a79b1f1c0271fbe79e844580bb598bafa1ed208b94da3cdcd42")
    version("3.10.0.2", sha256="49f75d16ff11f1cd258e1b988ccff82a3ca5570217d7ad8c5f48205dd99a677e")
    version("3.10.0.0", sha256="50b6f157849174217d0656f99dc82fe932884fb250826c18350e159ec6cdf342")
    version("3.7.4.3", sha256="99d4073b617d30288f569d3f13d2bd7548c3a7e4c8de87db09a9d29bb3a4a60c")
    version("3.7.4", sha256="2ed632b30bb54fc3941c382decfd0ee4148f5c591651c9272473fea2c6397d95")
    version("3.7.2", sha256="fb2cd053238d33a8ec939190f30cfd736c00653a85a2919415cecf7dc3d9da71")
    version("3.6.6", sha256="51e7b7f3dcabf9ad22eed61490f3b8d23d9922af400fe6656cb08e66656b701f")

    depends_on("python@3.8:", when="@4.8:", type=("build", "run"))
    # Needed to ensure that Spack can bootstrap with Python 3.6
    depends_on("python@3.7:", when="@4.2:", type=("build", "run"))
    depends_on("py-flit-core@3.4:3", when="@4:", type="build")

    # Historical dependencies
    depends_on("py-setuptools", when="@:3", type="build")
