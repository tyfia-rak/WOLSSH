/* Corriger la vérification de rSz */

if (rSz >= WOLFSSH_MAX_FILENAME || (int)(rSz + UINT32_SZ) > maxSz) {
    return WS_BUFFER_E;
}

