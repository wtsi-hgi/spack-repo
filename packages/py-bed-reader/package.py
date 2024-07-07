# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBedReader(PythonPackage):
    """Read and write the PLINK BED format, simply and efficiently."""

    homepage = "https://fastlmm.github.io/"
    pypi = "bed-reader/bed_reader-1.0.5b4.tar.gz"

    version(
        "0.2.23",
        sha256="07c189709b5319ffcb336a67dbaed108fc1931e89afac49ee08e6be04c4b589f",
        expand=False,
        url="https://files.pythonhosted.org/packages/f0/23/87569317213e8a0f3738eac535b37cd3f32267951ef6078e0b1ad01b3a3c/bed_reader-0.2.23-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.whl",
    )
    version(
        "0.2.24",
        sha256="a761cc6460ac0a0b538027a5bff41e9f016a1a8d6c3929613f0612fb295c163e",
        expand=False,
        url="https://files.pythonhosted.org/packages/cd/66/844c25732c6454f52785368af6ed9f556c037d50777d4b6c998493cc059e/bed_reader-0.2.24-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.whl",
    )
    version("0.2.29", sha256="fb0fb1a27e9bcd575fb4c78d9a976a6ef088a8c80d463cd78472bbaca8f75539")
    version("0.2.3", sha256="ac40477acefe2ff13b4e92b68a02663d861530d711953c295b3d54fb2d3ef25c")
    version("0.2.34", sha256="ec9f41a8df02d750c79adb7ace2adf0c1263de38c4db9ecdf0b2a0e40628b567")
    version("0.2.35", sha256="618af7c670595652873943b4ce6b2633efe1ac536666c46328d7d05cca4fecc8")
    version("0.2.36", sha256="9bbbd28117deef3ca00ec67553bd5f8fa8bd19919f316cb77316e6230158cca4")
    version("0.2.37", sha256="34057e06d8d2ed15e7fbdb6a9bf6b09a17f3b4740f5e0803b9a13a390bfeab98")
    version("0.2.5", sha256="e35158c771d0254df49ec8128e0976341f075bc8563c3b33df7cd1d87ea5d2b1")
    version(
        "0.2.6",
        sha256="e802b752bcc9ccab76e7a620cbc2f79ee4712d7bb080628fe179d237c28faf66",
        expand=False,
        url="https://files.pythonhosted.org/packages/ec/dc/db738aa4d57c23ff6688b6960d47b9e5535f252456eac21a7aaa1ab9282b/bed_reader-0.2.6-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.whl",
    )
    version(
        "0.2.7",
        sha256="4eddfd1451b16b2b944d87fde9707448790392c4fcd336cb1bb937fc9b392569",
        expand=False,
        url="https://files.pythonhosted.org/packages/6b/70/a7c74e5da8985bffc713f36ba5cbbe09ddd2a394341cea6a8110673d68f4/bed_reader-0.2.7-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.whl",
    )
    version(
        "0.2.8",
        sha256="49a3c82f539143569d99b4213572b963244d02311da28a6ebac258dcbf26a35c",
        expand=False,
        url="https://files.pythonhosted.org/packages/a7/35/293881cd95a599fa905113bfedd8eccf8d969131b17e4aa943b8ea0ba524/bed_reader-0.2.8-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.whl",
    )
    version(
        "0.2.9",
        sha256="df4f7224c3b6a2e2fde20539c66ae0bd929c05e67f124b08e28b34878517cf9a",
        expand=False,
        url="https://files.pythonhosted.org/packages/9a/9f/991e81ff50bbe1f757ba11f4c1978bda42e5933a9d72f127b81a5267277a/bed_reader-0.2.9-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.whl",
    )
    version("1.0.0", sha256="fea2ef4562ca3211b6087185d8ff73e60b75915066c10d2d1b398ab87ece4ed9")
    version("1.0.0b1", sha256="adf84439c8db34c4f815444e5976593abd9a1323cdaf0dff6e169363587a6d1b")
    version("1.0.0b3", sha256="e02c22802771697c66e92f742a36d6a17940f1f1ced9e4c707106f589cf078ec")
    version("1.0.0b4", sha256="b688de8df311d14e4c446f33d77887ffa45fe461f57c5552616ab1274c2b2b15")
    version("1.0.1b1", sha256="37888ee15f7ac01edc66ff4c87946a456694167c82d7b3e4d847a6e0be2704d7")
    version("1.0.1b2", sha256="d9e4c16ee1ebc04c1b9dc6debff047722a941f49169c2afe23d83170297e5fb5")
    version("1.0.1b5", sha256="7dc68161a59bfeab1eae6a8592610c2314f140af6aec3e230426650d242119eb")
    version("1.0.2", sha256="f7f862c642da3f8a64f0fcaa4564b314105a544496b156207eb1cdac655d3b6a")
    version("1.0.3", sha256="711926909a87c378cf3545cab9fbe6777a765e9aacb769d8d4b9cc21e70ee36a")
    version("1.0.3b1", sha256="3d2a8a9077e44bec87647bd187296cce32c38ca7ba5fc045b33e30c8f61d190b")
    version("1.0.4", sha256="a3c220fa496b1658926319ab0c68ae0cfe548f9637f338f54d195f7b934304e7")
    version("1.0.4b1", sha256="7b0eb9b4eb62ed012c2e1e79669ff9f846bcc3c176958e65fe951816a5117b90")
    version("1.0.4b2", sha256="f395974a08fc7c422b5db7bf452cb8b28ccac9adfc76a1d987591a1a835465c6")
    version("1.0.5", sha256="767ec321146691ac1d8816675c581a1ca08cfa08508deee39a741d12db836ef8")
    version("1.0.5b1", sha256="42daab2d36e5d32941b2c52008bb63534bd8f1e04e13ed87032728b4168cf378")
    version("1.0.5b2", sha256="8960e2dae2759cfb83fa8bc4492e8c90ef3881f965fb9c60332e51a27b2735ff")
    version("1.0.5b3", sha256="0371cdf14e445915284c04aa5f5936da10c0508cc1bcd502acd5c82262fc7572")
    version("1.0.5b4", sha256="f5385057e00afdce019c55846985cb293ceb85ceb56bb4d67c94da3de456a041")

    variant("samples", default=True)
    variant("sparse", default=False)
    depends_on("py-maturin", type="build")
    depends_on("py-numpy@1.13.3:", type=("build", "run"))
    depends_on("py-pooch@1.5:", type=("build", "run"), when="+samples")
    depends_on("py-scipy@1.4:", type=("build", "run"), when="+sparse")


# {'numpy>=1.13.3': ['0.2.23', '0.2.24', '0.2.6', '0.2.7', '0.2.8', '0.2.9'], 'pandas>=0.25.1': ['0.2.23', '0.2.24', '0.2.6', '0.2.7', '0.2.8', '0.2.9'], 'pooch>=1.1.1': ['0.2.23', '0.2.24', '0.2.6', '0.2.7', '0.2.8', '0.2.9']}
