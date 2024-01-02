# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RYaml(RPackage):
    """Implements the 'libyaml' 'YAML' 1.1 parser and emitter (<https://pyyaml.org/wiki/LibYAML>) for R."""

    homepage = "https://github.com/vubiostat/r-yaml/"
    cran = "yaml"

    version("2.3.7", sha256="d20cb219e0f9c48aba02f132f81cfa9ecda5e22c925e36726840218ed56680ab")
    version("2.3.6", sha256="5dd19d8d6654ef2e4ccd6216ce8e96ca5185ae6143f95194955f6908a6e1ba26")
    version("2.3.5", sha256="3edf6c0554a0e184a25e8bec5721a2e66b4ab0dceb3737428e22705e52eb5140")
    version("2.3.4", sha256="cb2625ada9996ebadd24930dae89fff6523366f82d07757e8b0ed260a0ff72a6")
    version("2.2.2", sha256="a5dc6aba2719eb4422bdd7d3a7b2223bbb00e4470fa234d8c5b3a6835d99f730")
    version("2.2.1", sha256="1115b7bc2a397fa724956eec916df5160c600c99a3be186d21558dd38d782783")
    version("2.2.0", sha256="55bcac87eca360ab5904914fcff473a6981a1f5e6d2215d2634344d0ac30c546")
    version("2.1.19", sha256="e5db035693ac765e4b5fe1fc2e9711f8ca73e398e3f2bf27cc60def59ccd7f11")
    version("2.1.18", sha256="1bb54d5f28f0adc24a5f3cfbf5cda4a71ca2ad7922a687f756e0619767c1a496")
    version("2.1.17", sha256="5af150d64be1f181c2ec3a6702ea2757202d36563089ac9c4963a22db6e5c683")
    version("2.1.16", sha256="75da4b175089b1634b532b5d4c4bf3eb72177c30c0a09e1333fc004315ae9af6")
    version("2.1.15", sha256="14293d84cde0cc0e84f7600b7a55de9236fc93f84d018fa6a080cfe8afe386d8")
    version("2.1.14", sha256="41a559846f6d44cc2dbcb3fc0becbc50d2766d3dc2aad7cfb97c1f9759ec0875")
    version("2.1.13", sha256="26f69aa2008bcacf3b2f95ef82a4667eaec2f2da8487646f71f1e2635d2d7fa2")
    version("2.1.12", sha256="1d169910c5424557358c65bfcaa655b37b7129610a9fe6f9dcf70685ea65d1cf")
    version("2.1.11", sha256="f5915a10c83fbfbbb0609a35482c2dff1dd33589d53d9dbae9afb46a7e6d3311")
    version("2.1.10", sha256="5d6def534f5c7879bfb652537cb273386c54755bbe3818fe82611e26f6128ae7")
    version("2.1.9", sha256="89fa3bd7a0e7aa09aeaec5b8293ffc06389c418494ea0dd61bc56c487b0d7f8c")
    version("2.1.8", sha256="fbc3a9bc06d852d61cd2f279288b3e066d2e73af1464cd3051471a2688b9e598")
    version("2.1.7", sha256="bd7f55b7e824177371d89e2375e702ad1fa34d5f2b8b70c4221be9fbc1ab8de0")
    version("2.1.6", sha256="c7c06c86f035151fab30e6e0a602d674d98eeb56345bab69e573b89639360d22")
    version("2.1.5", sha256="a9e203d7ca6cde2316abe3b7b65b9229da1f7081daacecbf671f9f899c7250cb")
    version("2.1.4", sha256="c0a78f0ae2df3253ff5b7bbb29f3773cb285f8f5ceb9116dac37bfdcf74d146b")
    version("2.1.3", sha256="b86c4944f01fe2a0df34e0129b66b5c876893ac0d84fd1b60eec6979973e7dc3")
    version("2.1.2", sha256="2f5e3313a182a48b00d6d96aed42f2639be3e9bfe632d8b749fe0c64cd444fb0")
    version("2.1.1", sha256="35123658696515b5068a5e6b5a96277998c1d5d8320c39eb22552366f1b2bff0")
    version("2.1.0", sha256="58f2a5b0f09069775153b945d089e7b26d7e87e2c0cbcca58e019cc47ed300a0")
    version("2.0.0", sha256="ea7f36fe8fe35de1acd8d2f84c3f38587017c8d7c7fe162ff8ceacd4a45e0ec2")
    version("1.2.0", sha256="d1aebfe7cbf8de866e47a0a6e7f28b7119d054a29df706ef256f016ee6c9ca2c")
    version("1.1.0", sha256="aeb17740e1e3deb0eb9c2e68f72213ebee745153c24d8a320294c01ce8be4d63")
    version("1.0.2", sha256="5ea10714e6204b24149f423c783ded6a196688306e5952edc2fbe443f96de4f6")
    version("1.0.1", sha256="39fd55d7cbc1b27d061249efab6e2aef4b6c00fe1264daf18c997ef0f01a2117")
    version("1.0", sha256="cce0b3e9590de00c67b4ab0bddc30ff60827688f782104ffebe5777b4d5f9d27")
