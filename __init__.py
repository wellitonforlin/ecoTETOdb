# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ecoTETOdb
                                 A QGIS plugin
 Solução de Geoinformação para a ONG TETO.
                             -------------------
        begin                : 2017-12-08
        copyright            : (C) 2017 by Welliton Forlin
        email                : welliton.forlin@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ecoTETOdb class from file ecoTETOdb.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ecoTETOdb import ecoTETOdb
    return ecoTETOdb(iface)
